import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateingComponent } from './createing.component';

describe('CreateingComponent', () => {
  let component: CreateingComponent;
  let fixture: ComponentFixture<CreateingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
