import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  public username: any = '';
  public password: any = '';
  public password2: any = '';
  public email: any = '';
  public logged = false;
  public completed = false;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.completed = false;
    const token = localStorage.getItem('token');
    if( token ){
      this.logged = true;
    }
  }
  signup(){
    if(this.password === this.password2 && this.password!=='' && this.username!=='' && this.email!==''){
      this.provider.signup(this.username,this.email,this.password).then( res =>{
        this.completed = true;
      }).catch( res =>{
        alert("User With That Name is Already Taken");
      })
    }else{
      alert("Something Does Not match");
    }
  }
  
}
