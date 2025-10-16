import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Pesquisa } from '../models/pesquisas';
import { environment } from "../../environments/environments"

type LivroQuery = {
  search?: string | null;
  titulo?: string | null;
  autor?: string | null;
  id?: number | string;
}

@Injectable({providedIn: 'root'})
export class PesquisasServices {
  private http = inject(HttpClient)
  private base = environment.apiBase

  listar(q?: LivroQuery): Observable<Pesquisa[]>{
    let params = new HttpParams() 
    
    if (q){
      Object.entries(q).forEach(([k, v]) => {

        if (v !== undefined && v !== null && String(v).trim() !== ''){
          params = params.set(k, String(v))
        }

      })
    }
    return this.http.get<Pesquisa[]>(this.base, {params})
  }
}
