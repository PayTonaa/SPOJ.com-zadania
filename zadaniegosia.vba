Option Explicit

Private Sub CommandButton1_Click()
    ' obliczenie wartości funkcji liniowej ax + b '
    Dim a As Double, b As Double, x As Double, y As Double
    a = CDbl(TextBox1.Value)
    b = CDbl(TextBox2.Value)
    x = CDbl(TextBox3.Value)
    y = a * x + b
    TextBox4.Value = CStr(y)
End Sub

Private Sub CommandButton2_Click()
    ' obliczenie wartości funkcji kwadratowej ax^2 + bx + c '
    Dim a As Double, b As Double, c As Double, x As Double, y As Double
    a = CDbl(TextBox5.Value)
    b = CDbl(TextBox6.Value)
    c = CDbl(TextBox7.Value)
    x = CDbl(TextBox8.Value)
    y = a * x ^ 2 + b * x + c
    TextBox9.Value = CStr(y)
End Sub

Private Sub CommandButton3_Click()
    ' obliczenie wartości funkcji wymiernej (a*x+b)/(c*x+d) '
    Dim a As Double, b As Double, c As Double, d As Double, x As Double, y As Double
    a = CDbl(TextBox10.Value)
    b = CDbl(TextBox11.Value)
    c = CDbl(TextBox12.Value)
    d = CDbl(TextBox13.Value)
    x = CDbl(TextBox14.Value)
    y = (a * x + b) / (c * x + d)
    TextBox15.Value = CStr(y)
End Sub

Private Sub TextBox4_Change()
    ' czyszczenie wyniku po zmianie wartości a, b lub x '
    TextBox4.Value = ""
End Sub

Private Sub TextBox9_Change()
    ' czyszczenie wyniku po zmianie wartości a, b, c lub x '
    TextBox9.Value = ""
End Sub

Private Sub TextBox15_Change()
    ' czyszczenie wyniku po zmianie wartości a, b, c, d lub x '
    TextBox15.Value = ""
End Sub

