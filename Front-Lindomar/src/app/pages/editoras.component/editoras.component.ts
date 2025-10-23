import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { EditorasServices } from '../../services/editoras.services';
import { Editora } from '../../models/editora';
import { AuthService } from '../../services/auth.services';
import { ɵInternalFormsSharedModule } from "@angular/forms";
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  imports: [RouterLink, ɵInternalFormsSharedModule, FormsModule, CommonModule],
  templateUrl: './editoras.component.html',
  styleUrls: ['./editoras.component.css']
})



export class EditorasComponent {
  filtro = '';
  sugestoes = signal<Editora[]>([]);

  private svc = inject(EditorasServices);
  private auth = inject(AuthService);   //Ver o token
  editoras = signal<Editora[]>([]);
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
      next: (data) => { this.editoras.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar editoras'); this.carregando.set(false); }
    });
  }
}