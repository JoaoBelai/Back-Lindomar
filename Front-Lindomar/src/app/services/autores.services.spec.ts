import { TestBed } from '@angular/core/testing';

import { AutoresServices } from './autores.services';

describe('AutoresServices', () => {
  let service: AutoresServices;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AutoresServices);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
