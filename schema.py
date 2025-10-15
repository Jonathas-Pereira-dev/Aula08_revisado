import pandera.pandas as pa
from pandera.typing import Series

#OLD class VendasSchema(pa.SchemaModel):
class VendasSchema(pa.DataFrameModel): #NEW
    Produto: Series[str]
    Categoria: Series[str]
    Quantidade: Series[int] = pa.Field(ge=0)  # ge=0 significa "maior ou igual a 0"
    Venda: Series[int] = pa.Field(ge=0)
    Data: Series[str]
    
    class Config:
        coerce = True
        strict = True