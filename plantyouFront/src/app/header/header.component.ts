import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  public registeredUsername: any = 'Log In';
  public logged = false;
  constructor() { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if ( token ) {
      this.logged = true;
      this.registeredUsername = localStorage.getItem('username');
    }
  }
}
