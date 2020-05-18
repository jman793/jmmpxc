import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginPageComponent } from './login-page/login-page.component';
import { LandingComponent } from './landing/landing.component';
import { InsertPageComponent } from './insert-page/insert-page.component';


const routes: Routes = [
  {path: '', component: LoginPageComponent},
  {path: 'page',component: LandingComponent},
  {path:'insert',component: InsertPageComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
