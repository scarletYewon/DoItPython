from queue import PriorityQueue

# 선언
N = int(input())
plusPq = PriorityQueue() # 양수큐
minusPq = PriorityQueue() # 음수큐
one = 0 # 1의 개수
zero = 0 # 0의 개수

# 입력
for i in range(N):
  data = int(input())
  if data >1:
    plusPq.put(data*-1) # 내림차순 정렬을 위해 -1일 곱하여 저장
  elif data ==1:
    one +=1
  elif data ==0:
    zero +=1
  else:
    minusPq.put(data)

# 우선순위 큐이기 때문에 도출된 합이 최대임
sum = 0

# 양수큐에서 큐사이즈가 1개 또는 0개가 될때까지 큰수 두개 곱해서 합에 더해줌
while plusPq.qsize()>1:
  first = plusPq.get()
  second = plusPq.get()
  sum += first*second

# 양수큐의 큐사이즈가 1개이면 -1일 곱해서 더해줌
if plusPq.qsize()>0:
  sum+= plusPq.get()*-1

# 음수큐에서 큐사이즈가 1개 또는 0개가 될때까지 큰수 두개 곱해서 합에 더해줌
while minusPq.qsize()>1:
  first = minusPq.get()
  second = minusPq.get()
  sum += first*second

# 음수큐의 큐사이즈가 1개이면 그냥 더해줌
if minusPq.qsize()>0:
  sum+= minusPq.get()

# 1처리
sum += one

print(sum)