import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {LoginComponent} from './login/login.component';
import {MainComponent} from './main/main.component';
import {SignupComponent} from './signup/signup.component';
import {AboutusComponent} from './aboutus/aboutus.component';
import {CatalogComponent} from './catalog/catalog.component';
import {EditfoodComponent} from './editfood/editfood.component';
import {CreatefoodComponent} from './createfood/createfood.component';
import {CreateingComponent} from './createing/createing.component';

const routes: Routes = [
  {path: '', component: MainComponent},
  {path: 'login', component: LoginComponent},
  {path: 'signup', component: SignupComponent},
  {path: 'aboutus', component: AboutusComponent},
  {path: 'catalog', component: CatalogComponent},
  {path: 'editfood', component: EditfoodComponent},
  {path: 'createfood', component: CreatefoodComponent},
  {path: 'createing', component: CreateingComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
