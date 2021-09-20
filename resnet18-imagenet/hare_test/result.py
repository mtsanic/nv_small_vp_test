f=open("output.dimg","r" )
content=f.read()
content_list=content.split(" ")
max_val=max(content_list)

max_index=content_list.index(max_val)

print(max_val, max_index)

print(min(content_list), content_list.index(min(content_list)))

print(len(content_list))

print(max(content))
g_colour_list=[]
ff=open("synset_words.txt", "r")
for line in ff:
    g_colour_list.append(int(line.strip('\n')))

print(len(g_colour_list))

