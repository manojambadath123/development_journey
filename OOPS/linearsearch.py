


class LinearSearch:

    def solution(self,arr,element):

        is_present = False

        for num in arr:

            if num==element:

                is_present=True
                break


        return is_present
    
le_instance = LinearSearch()

arr=[10,11,12,13,14,14]
element=13

print(le_instance.solution(arr,element))