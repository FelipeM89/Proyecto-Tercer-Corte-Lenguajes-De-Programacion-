"""
LibreriaPerceptronMC.py
Implementación de un perceptrón multicapa (MLP) sin dependencias.
Clase: PerceptronMulticapa
 - __init__(layers, lr, seed)
 - fit(X, Y, epochs, batch_size, verbose)
 - predict(x)
 - score(X,Y) -> mse
 - loss_history
"""

from Librerias.LibreriaAritmentica import LCG, exp

def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))

def dsigmoid(x):
    s = sigmoid(x)
    return s * (1.0 - s)

class PerceptronMulticapa:
    def __init__(self, layers, learning_rate=0.1, seed=1234):
        """
        layers: list of ints e.g. [input_dim, h1, h2, output_dim]
        """
        self.layers = layers[:]
        self.lr = learning_rate
        self.seed = int(seed)
        self.rng = LCG(self.seed)
        self.weights = []  # list of matrices: pesos por capa (neurons x inputs)
        self.biases = []   # list of bias vectors per capa
        self.loss_history = []
        # inicializar pesos pequeños
        for i in range(len(layers)-1):
            in_dim = layers[i]
            out_dim = layers[i+1]
            W = [[(self.rng.rand() - 0.5) * 0.2 for _ in range(in_dim)] for _ in range(out_dim)]
            b = [(self.rng.rand() - 0.5) * 0.2 for _ in range(out_dim)]
            self.weights.append(W)
            self.biases.append(b)

    def _forward_single(self, x):
        a = x[:]  # activaciones
        activations = [a]
        zs = []
        for W,b in zip(self.weights, self.biases):
            z = []
            a_next = []
            for j in range(len(W)):
                s = b[j]
                for i in range(len(W[j])):
                    s += W[j][i] * a[i]
                z.append(s)
                a_next.append(sigmoid(s))
            zs.append(z)
            activations.append(a_next)
            a = a_next
        return activations, zs

    def _backprop_single(self, x, y):
        activations, zs = self._forward_single(x)
        # convert y to vector if scalar
        y_vec = y[:] if isinstance(y, list) else [y]
        # compute delta for last layer
        L = len(self.weights)
        delta = []
        last_z = zs[-1]
        last_a = activations[-1]
        for j in range(len(last_a)):
            err = last_a[j] - y_vec[j]
            delta.append(err * dsigmoid(last_z[j]))
        nabla_w = [None]*L
        nabla_b = [None]*L
        # last layer gradients
        nabla_b[L-1] = delta[:]
        nabla_w[L-1] = [[delta[j] * activations[-2][i] for i in range(len(activations[-2]))] for j in range(len(delta))]
        # propagate backwards
        for l in range(L-2, -1, -1):
            z = zs[l]
            sp = [dsigmoid(zj) for zj in z]
            delta_next = [0.0]*len(self.weights[l][0]) if len(self.weights[l][0])>0 else [0.0]
            # compute delta for layer l
            delta_l = [0.0]*len(self.weights[l])
            for i_neur in range(len(self.weights[l])):
                s = 0.0
                for k in range(len(delta)):
                    s += self.weights[l+1][k][i_neur] * delta[k]
                delta_l[i_neur] = s * sp[i_neur]
            # store gradients
            nabla_b[l] = delta_l[:]
            prev_a = activations[l]
            nabla_w[l] = [[delta_l[j] * prev_a[i] for i in range(len(prev_a))] for j in range(len(delta_l))]
            delta = delta_l
        return nabla_w, nabla_b

    def _update_mini_batch(self, nabla_w_sum, nabla_b_sum, batch_size):
        for l in range(len(self.weights)):
            for j in range(len(self.weights[l])):
                for i in range(len(self.weights[l][j])):
                    self.weights[l][j][i] -= (self.lr / batch_size) * nabla_w_sum[l][j][i]
            for j in range(len(self.biases[l])):
                self.biases[l][j] -= (self.lr / batch_size) * nabla_b_sum[l][j]

    def fit(self, X, Y, epochs=1000, batch_size=1, verbose=False):
        n = len(X)
        for ep in range(epochs):
            total_loss = 0.0
            # simple SGD without shuffling (deterministic)
            for i in range(0, n, batch_size):
                end = min(i+batch_size, n)
                nabla_w_sum = [ [ [0.0 for _ in row] for row in W ] for W in self.weights ]
                nabla_b_sum = [ [0.0 for _ in b] for b in self.biases ]
                bs = end - i
                for j in range(i, end):
                    x = X[j]
                    y = Y[j]
                    nw, nb = self._backprop_single(x, y)
                    # accumulate
                    for l in range(len(self.weights)):
                        for a in range(len(nw[l])):
                            for b_idx in range(len(nw[l][a])):
                                nabla_w_sum[l][a][b_idx] += nw[l][a][b_idx]
                        for a in range(len(nb[l])):
                            nabla_b_sum[l][a] += nb[l][a]
                    # compute sample loss
                    pred = self.predict(x)
                    # flatten pred and y
                    p_flat = pred if isinstance(pred, list) else [pred]
                    y_flat = y if isinstance(y, list) else [y]
                    for a,bv in zip(p_flat, y_flat):
                        total_loss += (a - bv) ** 2
                # update weights
                self._update_mini_batch(nabla_w_sum, nabla_b_sum, bs)
            self.loss_history.append(total_loss)
            if verbose and (ep % max(1, epochs//10) == 0):
                print("Epoch", ep, "loss", total_loss)
        return self

    def predict(self, x):
        a = x[:] if isinstance(x, list) else [x]
        for W,b in zip(self.weights, self.biases):
            a_next = []
            for j in range(len(W)):
                s = b[j]
                for i in range(len(W[j])):
                    s += W[j][i] * a[i]
                a_next.append(sigmoid(s))
            a = a_next
        return a if len(a) > 1 else a[0]

    def score(self, X, Y):
        # returns mse
        preds = []
        ys = []
        for x,y in zip(X,Y):
            p = self.predict(x)
            if isinstance(p, list):
                preds.append(p[0])
            else:
                preds.append(p)
            if isinstance(y, list):
                ys.append(y[0])
            else:
                ys.append(y)
        # compute mse
        n = len(preds)
        total = sum((preds[i] - ys[i])**2 for i in range(n))
        return total / n if n>0 else 0.0