charaters=[]
start={}
with open("xyj.txt","r",encoding="UTF-8") as nfile:
     for line in nfile:
     		line=line.strip()
     		if(len(line)==0):
     			continue
     		for x in range(0,len(line)):
     			if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
     				continue
     			if not line[x] in charaters:
     				charaters.append(line[x])
     			if not start.get(line[x]):
     				start[line[x]]=0
     			start[line[x]] +=1
print(len(charaters))
print(len(start))
start = sorted(start.items(), key=lambda d:d[1], reverse=True)
with open("res.txt","w",encoding="UTF-8") as rfile:
	for item in start:
		rfile.write(item[0]+","+str(item[1])+"\n")


