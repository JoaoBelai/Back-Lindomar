import { Component } from "@angular/core";
import { RouterLink } from "@angular/router";

@Component({
    selector:'app-home',
    standalone: true,
    imports: [RouterLink],
    styleUrl: './home.component.css',

    template: `
    <section>
      <h1>Bem-vindo</h1>
      <p>Esta é a página inicial.</p>

      <nav>
        <a routerLink="/autores">Ver autores</a>
        <a routerLink="/editoras">Ver editoras</a>
        <a routerLink="/livros">Ver livros</a>
        <a routerLink="/pesquisas">Pesquisar Livro</a>

      </nav>
    </section>
  `
})

export class HomeComponent {}