' Keep track of the location for each Ticker in the summary table

 Dim Summary_Table_Row As Integer
 Summary_Table_Row = 2
 

For i = 2 To 43398

' Set ticker name
Ticker = Cells(i, 1).Value

' Calculate and add to ticker total
Ticker_Total = Ticker_Total + Cells(i, 7).Value

' Check if we are still within the same ticker
If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

' Print the ticker in the Summary Table
Range(“I” & Summary_Table_Row).Value = Ticker

' Print the Ticker_Total to the Summary Table
Range(“J” & Summary_Table_Row).Value = Ticker_Total

' Add one to the summary table row
Summary_Table_Row = Summary_Table_Row + 1
     
     ' Reset the Ticker_Total
     Ticker_Total = 0

   ' If the cell immediately following a row is the same ticker...
   Else
   
   Ticker_Total = Ticker_Total + Cells(i, 7).Value
    ’MsgBox (ticker_Total)
   
   End If

Next i

End Sub