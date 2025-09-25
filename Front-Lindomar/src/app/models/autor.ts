export interface Autor{
    id: number,
    nome: string,
    sobrenome: string,
    data_nascimento: string,
    nacionalidade ?: string | null,
    biografia?: string | null;
}