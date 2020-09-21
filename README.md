# Program and Testing Assignment
| Input Name | Valid Data Type | Where does it come from | Valid Value (s) | Tests |
|------------|-----------------|-------------------------|-----------------|-------|
| Subtotal | Float | Manual Entry (Check Subtotal) | Any positive real number, less than or equal to 1 million dollars | Value < .01 (invalid) Value > 1000000 (invalid), Value == .01 (valid), Value == 1000000 (valid)

| Output Name | Valid Data Type | Where does it come from | Valid Value (s) | Tests |
|------------|-----------------|-------------------------|-----------------|-------|
| Grand Total | Float | Subtotal + Tip |  Any positive real number, less than or equal to 1 million dollars. Also, greater than Subtotal. | Value < .01 (invalid) Value > 1000000 (invalid), Value == .01 (valid), Value == 1000000 (valid), Grand Total > Subtotal