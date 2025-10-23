import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AutoresServices } from '../../services/autores.services';
import { Autor } from '../../models/autor';
import { AuthService } from '../../services/auth.services';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  imports: [RouterLink, FormsModule, CommonModule],
  templateUrl:'./authors.component.html',
  styleUrls: ['./authors.component.css']
})
export class AutoresComponent {

  filtro = '';
  sugestoes = signal<Autor[]>([]);

  private svc = inject(AutoresServices);
  private auth = inject(AuthService);   //Ver o token
  autores = signal<Autor[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  buscar(){
    const parametro = this.filtro.trim();
    if(parametro.length < 2){
      this.sugestoes.set([]);
      return;
    }

    this.svc.listar(parametro).subscribe({
      next: (data) =>{
        this.sugestoes.set(data.slice(0,3));
      },
      error: () => this.sugestoes.set([]),
    });
  }

  constructor() {
    console.log("Token de acesso: ", this.auth.token());
    
    this.svc.listar().subscribe({
      next: (data) => { this.autores.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar autores'); this.carregando.set(false); }
    });
  }
}