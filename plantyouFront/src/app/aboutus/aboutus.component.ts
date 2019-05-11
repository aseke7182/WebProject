import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Developer} from '../models/models';

@Component({
  selector: 'app-aboutus',
  templateUrl: './aboutus.component.html',
  styleUrls: ['./aboutus.component.css']
})
export class AboutusComponent implements OnInit {
  
  public developers: Developer[] = [];
  constructor(private provider:ProviderService ) { }

  ngOnInit() {
    this.getDevelopers();
  }
  getDevelopers(){
    this.provider.getDevelopers().then(res =>{
      this.developers = res;
    }).catch(res =>{
      alert("SOMETHING WRONG");
    })
  }

}
