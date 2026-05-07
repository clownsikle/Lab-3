import Lab2.BMI_Calculator 

def test_bmi_normal_weight():
    assert(Lab2.BMI_Calculator.calculate(1.67,67) == 0)
def test_bmi_over_weight():
    assert(Lab2.BMI_Calculator.calculate(1.67,100) == 1)
def test_bmi_under_weight():
    assert(Lab2.BMI_Calculator.calculate(1.67,40) == -1)