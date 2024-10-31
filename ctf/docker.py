from pwn import *

# 连接到 WebSocketReflectorX 给出的本地端口
port =53729 # 将 <port> 替换为实际的端口号
connection = remote('127.0.0.1', port)

# 发送任意需要的命令或者数据
# 示例：如果需要发送某个初始请求
# connection.sendline('some_initial_data')

# 接收服务器的响应
response = connection.recv()
print(response)

# 如果服务器直接返回了 flag，那么就可以直接读取输出
flag = response.decode()
print(f"The flag is: {flag}")

# 关闭连接
connection.close()
