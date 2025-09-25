import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresComponent } from './pages/authors.component/authors.component';
import { EditorasComponent } from './pages/editoras.component/editoras.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresComponent},
    {path: 'editoras', component: EditorasComponent}
];
