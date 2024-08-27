class ClassRoom():
    def __init__(self,name=[],grade=0,homeRoomTeacher: str="",numStudents : int=0):
        self.name = name 
        self.grade = grade
        self.homeRoomTeacher = homeRoomTeacher
        self.numStudents = numStudents
        
    def set_student_list(self,name):
        self.name = name
        
    def set_grade(self,grade: int):
        self.grade = grade
        
    def set_homeroom_teacher(self,homeRoomTeacher: str):
        self.homeRoomTeacher = homeRoomTeacher
    
    def set_num_student(self,numStudents: int):
        self.numStudents = numStudents
    
    def get_grade(self) ->int:
        return self.grade
        
    def get_homeroom_teacher(self) ->str:
        return self.homeRoomTeacher
    
    def get_student_list(self):
        return self.name
    
    def get_num_student(self) ->int:
        return self.numStudents
    def get_student_no(self,n) ->int:
        return self.name[n-1]

    def add_student(self,student_name: str):
        '''if student_name not in self.name:
            self.name.append(student_name)
            return True
        else: return False'''
        if self.numStudents==10:
            return False
        else:
            self.name.append(student_name)
            self.numStudents+=1
            return True
    def change_student(self,n, new_name):
        if n>=1 and n<=len(self.name):
            self.name[n-1] = new_name
            return True
        else: return False
    def remove_student(self,student_name):
        if student_name in self.name:
            self.numStudents -= 1
            self.name.remove(student_name)
            
            return True
        else:
            return False
    def remove_student_no(self,n):
        if n>=1 and n<=len(self.name):
            self.name.pop(n-1)
            self.numStudents-=1
            return True
        else: return False
    def __str__(self):
        x = ", ".join(self.name)
        return f'Grade: {self.grade}\nHomeroom Teacher: {self.homeRoomTeacher}\nStudents: {x}'
    
