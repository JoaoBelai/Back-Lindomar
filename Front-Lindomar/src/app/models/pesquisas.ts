export interface Pesquisa{
    id:Number,
    titulo: String,
    subtitulo: String,
    autor: Number,
    editora: Number,
    isbn: String,
    descricao: String,
    idioma: String,
    ano_publicacao: Number,
    paginas: Number,
    preco: Number,
    estoque: Number,
    desconto?: Number | null,
    disponivel: Boolean,
    dimensoes?: String | null,
    peso?: Number| null
}