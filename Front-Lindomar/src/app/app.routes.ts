import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresComponent } from './pages/authors.component/authors.component';
import { EditorasComponent } from './pages/editoras.component/editoras.component';
import { LivrosComponent } from './pages/livros.component/livros.component';
import { LoginComponent } from './pages/login.component/login.component';
import { authGuard } from './auth.guard';

export const routes: Routes = [
    
    {path: '', component: LoginComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresComponent},
    {path: 'editoras', component: EditorasComponent},
    {path: 'livros', component: LivrosComponent},
    {path: 'pesquisas', component: LivrosComponent}

    // {path: '', component: LoginComponent},
    // {path: 'home', component: HomeComponent, canActivate: [authGuard]},
    // {path: 'autores', component: AutoresComponent, canActivate: [authGuard]},
    // {path: 'editoras', component: EditorasComponent, canActivate: [authGuard]},
    // {path: 'livros', component: LivrosComponent, canActivate: [authGuard]},
    // {path: 'pesquisas', component: LivrosComponent, canActivate: [authGuard]}
];
