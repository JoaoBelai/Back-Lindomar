import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresComponent } from './pages/authors.component/authors.component';
import { EditorasComponent } from './pages/editoras.component/editoras.component';
import { LivrosComponent } from './pages/livros.component/livros.component';
import { LoginComponent } from './pages/login.component/login.component';

export const routes: Routes = [
    {path: '', component: LoginComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresComponent},
    {path: 'editoras', component: EditorasComponent},
    {path: 'livros', component: LivrosComponent},
];
