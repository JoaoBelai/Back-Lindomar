import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Livro } from '../models/livro';
import { environment } from "../../environments/environments"



@Injectable({providedIn: 'root'})
export class LivrosServices {
  private http = inject(HttpClient)
  private base = environment.apiBase

  listar(filtro: string = ''): Observable<Livro[]>{
    let url = `${this.base}api/livros`
    if(filtro){
      url+= `/?titulo=${encodeURIComponent(filtro)}`
    }
    return this.http.get<Livro[]>(url)
  }
}
