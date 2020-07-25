import numpy as np

class NeuralNetwork:
    
    #cmd t1 x
    #cmd t2
    def __init__(self):
        # 将权重转化为一个3x1的矩阵，其值分布为-1~1，并且均值为0
        self.synaptic_weights = np.random.rand(3, 1)

    def sigmoid(self, x):
        # 应用sigmoid激活函数
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        #计算Sigmoid函数的偏导数
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):

        # 训练模型
        for iteration in range(training_iterations):
            # 得到输出
            output = self.think(training_inputs)

            # 计算误差
            error = training_outputs - output

            # 微调权重
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        # 输入通过网络得到输出
        # 转化为浮点型数据类型

        inputs = inputs.astype(np.float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

if __name__ == "__main__":

    # 初始化神经类
    neural_network = NeuralNetwork()
    print (neural_network.synaptic_weights)

    #训练数据
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    # 开始训练
    neural_network.train(training_inputs, training_outputs, 15000)

    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)

    user_input_one = str(input("User Input One: "))
    user_input_two = str(input("User Input Two: "))
    user_input_three = str(input("User Input Three: "))

    print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
    print("New Output data: ")
    print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
    print("Wow, we did it!")