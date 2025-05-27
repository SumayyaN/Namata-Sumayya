class ReportCard:
    # Mimicing method overloading using default and *args since Python doesn't natively support method overloading
    def print_report(self, student_name=None, grade=None):
        if student_name and grade:
            print(f"{student_name} has scored {grade}")
        elif student_name:
            print(f"Report for {student_name}")
        else:
            print("Generic Report")

card = ReportCard()
card.print_report()                         
card.print_report("sumayya")                 
card.print_report("Namata", "A")               
