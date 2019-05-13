import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public logged = false;
  public username: any = '';
  public password: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if ( token ) {
      this.logged = true;
    }
  }
  login() {
    // tslint:disable-next-line:no-conditional-assignment no-non-null-assertion triple-equals
    if (this.username! == '' && this.password! == '') {
      this.provider.login(this.username, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.username = '';
        this.password = '';
      }).catch(res => {
        alert('Username or Password is Incorrect');
        this.username = '';
        this.password = '';
      });
    } else {
      alert('WRITE SOMETHING!');
    }
  }
  logout() {
    this.provider.logout().then(res => {
      localStorage.clear();
      this.username = '';
      this.password = '';
      this.logged = false;
    }).catch( res => {
      alert('ERROR');
    });
  }

}
