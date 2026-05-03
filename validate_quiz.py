import re
with open(r'e:\CODEX UPLOADED TEST\data-quiz.JS', 'r', encoding='utf-8') as f:
    content = f.read()
start = content.index('{', content.index('const quizBank'))
depth = 0
end = -1
for i in range(start, len(content)):
    if content[i] == '{': depth += 1
    elif content[i] == '}': depth -= 1
    if depth == 0:
        end = i + 1
        break
obj = content[start:end]
print(f'Open braces: {obj.count("{")}, Close braces: {obj.count("}")}')
print(f'Open brackets: {obj.count("[")}, Close brackets: {obj.count("]")}')
mcqs = len(re.findall(r'o:\s*\[', obj))
tfs = len(re.findall(r'a:\s*(true|false)', obj))
fibs = len(re.findall(r'a:\s*\["', obj))
print(f'MCQs: {mcqs}, TFs: {tfs}, FIBs: {fibs}, Total: {mcqs+tfs+fibs}')
bal = 'BALANCED' if obj.count('{') == obj.count('}') and obj.count('[') == obj.count(']') else 'MISMATCH'
print(bal)
