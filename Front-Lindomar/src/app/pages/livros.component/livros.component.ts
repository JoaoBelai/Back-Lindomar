import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LivrosServices } from '../../services/livros.services';
import { Livro } from '../../models/livro';
import { AuthService } from '../../services/auth.services';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  imports: [RouterLink, FormsModule, CommonModule],
  templateUrl: './livros.component.html',
  styleUrls: ['./livros.component.css']

})
export class LivrosComponent {
  filtro = '';
  sugestoes = signal<Livro[]>([]);

  private svc = inject(LivrosServices);
  private auth = inject(AuthService);   //Ver o token
  livros = signal<Livro[]>([]);
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
      next: (data) => { this.livros.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar livros'); this.carregando.set(false); }
    });
  }
}