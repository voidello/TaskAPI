from pydantic import BaseModel
from datetime import datetime

class UsuarioBase(BaseModel):
    nome: str
    senha: str
    nivel_prioridade: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(BaseModel):
    id: int
    nome: str
    nivel_prioridade: str

    class Config:
        from_attributes = True

class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    data_vencimento: datetime
    status: str
    categoria_id: int

class TarefaCreate(TarefaBase):
    pass

class TarefaOut(BaseModel):
    id: int
    titulo: str
    descricao: str
    data_vencimento: datetime
    status: str
    categoria: CategoriaOut

    class Config:
        from_attributes = True
