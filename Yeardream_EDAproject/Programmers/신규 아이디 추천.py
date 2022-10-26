def solution(new_id):
    # 1
    new_id = new_id.lower()
    
    # 2
    words = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = "".join([word for word in new_id if word in words])
    
    # 3
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    #4
    if new_id[0] == "." and len(new_id) > 1:
      new_id = new_id[1:]
    if new_id[-1] == ".":       
      new_id = new_id[:-1]
    
    # 5
    if len(new_id) < 1 :
      new_id = "a"

    # 6
    if len(new_id) >= 16:
      new_id = new_id[:15]
    if new_id[-1] == ".":
      new_id = new_id[:-1]

    # 7
    if len(new_id) < 3:
      new_id = new_id + new_id[-1] * (3 - len(new_id))
    
    answer = new_id
    
    return answer
