from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", revision="v0.1.0",trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", revision="v0.1.0",trust_remote_code=True).half().cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
response, history = model.chat(tokenizer, "你是谁", history=history)
print(response)