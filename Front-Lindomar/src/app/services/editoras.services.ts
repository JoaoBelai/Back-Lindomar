import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Editora } from '../models/editora';
import { environment } from "../../environments/environments"



@Injectable({providedIn: 'root'})
export class EditorasServices {
  private http = inject(HttpClient)
  private base = environment.apiBase

  listar(filtro: string = ''): Observable<Editora[]>{
    let url = `${this.base}api/editoras`
    if(filtro){
      url+= `/?editora=${encodeURIComponent(filtro)}`
    }
    return this.http.get<Editora[]>(url)
  }
}
