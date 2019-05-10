import { Injectable } from '@angular/core';
import {Catalog,Food,Auth} from '../models/models';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService  {

  constructor(http: HttpClient) {
    super(http);
   }

  signup(username: any, email: any, password: any): Promise<Auth>{
    return this.post('http://127.0.0.1:8000/api/signup/',{
      username: username,
      email: email,
      password: password
    })
  }
  login(username: any , password: any): Promise<Auth>{
    return this.post('http://127.0.0.1:8000/api/login/',{
      username: username,
      password: password
    })
  }
  logout(): Promise<any>{
    return this.post('http://127.0.0.1:8000/api/logout/',{})
  }
}
