def brackets_of_n_order(sql_code,order):
    result_n_order={}
    result=[]
    Paranthesis_order=[]
    Paranthesis_index=[]
    string=''
    
    for letter in range(len(sql_code)):
        if sql_code[letter]=='(':
            Paranthesis_order.append(sql_code[letter])
            Paranthesis_index.append(letter)
        if sql_code[letter]==')':
            Paranthesis_order.append(sql_code[letter])
            Paranthesis_index.append(letter)
            
    while Paranthesis_order!=[]:
        a=1
        while Paranthesis_order[Paranthesis_order.index(')')-a]==')':
            a=a+1
        result.append(sql_code[Paranthesis_index[Paranthesis_order.index(')')-a]:Paranthesis_index[Paranthesis_order.index(')')]+1])
        Paranthesis_index.remove(Paranthesis_index[Paranthesis_order.index(')')-a])
        Paranthesis_order.remove(Paranthesis_order[Paranthesis_order.index(')')-a])
        Paranthesis_index.remove(Paranthesis_index[Paranthesis_order.index(')')])
        Paranthesis_order.remove(Paranthesis_order[Paranthesis_order.index(')')])
        
    for code in result:
        brackets=0
        for letter in code:
            if letter=='(':
                brackets=brackets+1
        else:
            if brackets not in result_n_order.keys():
                result_n_order[brackets]=[]
            result_n_order[brackets].append(code)

    #for n in range(max(list(result_n_order.keys())),0,-1):            
    return result_n_order[order]
            

code='''SELECT 
    employee.id,
    employee.first_name,
    employee.last_name,
    call.start_time, 
    call.end_time,
    DATEDIFF("SECOND", call.start_time, call.end_time) AS call_duration,
    duration_sum.call_duration_sum,
    CAST( CAST(DATEDIFF("SECOND", call.start_time, call.end_time) AS DECIMAL(7,2)) / CAST(duration_sum.call_duration_sum AS DECIMAL(7,2)) AS DECIMAL(4,4)) AS call_percentage
FROM call
INNER JOIN employee ON call.employee_id = employee.id
INNER JOIN (
    SELECT 
        employee.id,
        SUM(DATEDIFF("SECOND", call.start_time, call.end_time)) AS call_duration_sum
    FROM call
    INNER JOIN employee ON call.employee_id = employee.id
    GROUP BY
        employee.id
) AS duration_sum ON employee.id = duration_sum.id
ORDER BY
    employee.id ASC,
    call.start_time ASC;'''       
print(brackets_of_n_order(code,1))
