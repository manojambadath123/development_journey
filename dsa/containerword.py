
source = "traviduxtechnology"

target = "vridautx"

is_present = True

for ch in target:

    if ch not in source:

        is_present=False
        break

print(is_present)



source = "traviduxtechnology"

target = "vridautx"


set_a = set(source)

set_b = set(target)

present = set_b.issubset(set_a)


print(present)


class ContainerWord:

    def solution(self,source:str,target:str):

        is_present = True

        for ch in target:

            if ch not in source:

                is_present = False

                break

        return is_present
    
cnw_instance = ContainerWord()

print(cnw_instance.solution("traviduxtechnology","vridautx"))




class ContainerWord:

    def solution(self,source:str,target:str):

        

        present = set(target).issubset(source)

        return present
    
cnw_instance = ContainerWord()

print(cnw_instance.solution("traviduxtechnology","vridautx"))