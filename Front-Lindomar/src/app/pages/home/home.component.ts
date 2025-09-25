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
        <a routerLink="autores">Ver autores</a>
      </nav>
    </section>
  `
})

export class HomeComponent {}