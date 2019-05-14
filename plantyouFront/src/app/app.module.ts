import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ClassProvider } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './login/login.component';
import { MainComponent } from './main/main.component';
import { SignupComponent } from './signup/signup.component';
import { AboutusComponent } from './aboutus/aboutus.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import {ProviderService} from './services/provider.service';
import {FormsModule} from '@angular/forms';
import {Auth} from './Auth';
import { CatalogComponent } from './catalog/catalog.component';
import { EditfoodComponent } from './editfood/editfood.component';
import { CreatefoodComponent } from './createfood/createfood.component';
import { CreateingComponent } from './createing/createing.component'

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    MainComponent,
    SignupComponent,
    AboutusComponent,
    CatalogComponent,
    EditfoodComponent,
    CreatefoodComponent,
    CreateingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    ProviderService,
    <ClassProvider> {
      provide: HTTP_INTERCEPTORS,
      useClass: Auth,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
