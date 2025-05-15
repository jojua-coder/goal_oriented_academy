#1 Create Phone Number
def create_phone_number(n):
    return  f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


#2 Find the odd int
def find_it(seq):
    result=[]
    for i in seq:
        count=seq.count(i)
        if count %2==1:
            result.append(i)
    return result[0]

#3 Was the package received before it was sent? (Simplified)
def was_package_received_yesterday(tz_from, tz_to, start, duration):
    utc_start = start - tz_from
    utc_delivery = utc_start + duration
    local_delivery = utc_delivery + tz_to

    return local_delivery < 0
        