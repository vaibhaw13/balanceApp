import tabula

class PdfToCsv(object):
    
    def toCSV(self, path="~/Desktop/balanceapp/BalSheet.pdf"):

        try:
            df = tabula.read_pdf(
                path, 
                pages=1, 
                # output_format="json",
                stream=True,
                area=[130.05,47.25,505.35,685.35]
            )
            print(df[0], 'PDF file')

            dataFrame = df[0]
            # dataFrame.rename()
            #fix the mixup of 3rd and 4th columns
            columnNameMixed = dataFrame.columns[2]
            columnName1, columnName2 = columnNameMixed.split(' ')
            dataFrame[[columnName1+'_to', columnName2+'_by']] = dataFrame[columnNameMixed].str.split(' ', 1, expand=True)
            del dataFrame[columnNameMixed]
            del dataFrame['Unnamed: 0']

            allColumns = dataFrame.columns.tolist()
            reorderColumns= allColumns[:2] + allColumns[-2:] + allColumns[2:-2]
            dataFrame.to_csv(path.replace('pdf','csv'), index = False, header=True, columns=reorderColumns)

        except Exception:
            print('Could not convert the pdf file', Exception)
        
    def convertPdfToCSV(self, path="~/Desktop/balanceapp/BalSheet.pdf"):
        tabula.convert_into(path, "output.csv", output_format="csv", pages='all')

if __name__ == "__main__":
    o = PdfToCsv()
    print('Converting')
    o.toCSV()