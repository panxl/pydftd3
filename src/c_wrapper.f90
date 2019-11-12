!> Calculates the dispersion for a given non-periodic configuration.
!!
!! \param coords  Coordinates of the atoms in atomic units. Shape: [3, natoms].
!! \param izp  Atomic number of each atom. Shape: [natoms].
!! \param pars  Parameter to use. The 5 parameters must follow the same
!!     order as when specified in the dftd3.local file for the dftd3 program.
!!     (see the documentation of the dftd3 program for details)
!! \param version  Version to use. Note, that depending on the version the
!!     five parameters may have different (or no) meaning.
!! \param disp  Calculated dispersion energy in atomic units.
!! \param grads  Calculated gradients in atomic units.
!!
subroutine dftd3_dispersion_c(natoms, coords, izp, pars, version, disp, grads) &
     & bind(C, name="dftd3_dispersion")

  use iso_c_binding, only: c_int, c_double
  use dftd3_api, only: dftd3_input, dftd3_calc, dftd3_init, &
     & dftd3_set_params, dftd3_dispersion

  implicit none

  integer(kind=c_int), intent(in) :: natoms
  real(kind=c_double), intent(in) :: coords(3,natoms)
  integer(kind=c_int), intent(in) :: izp(natoms)
  real(kind=c_double), intent(in) :: pars(5)
  integer(kind=c_int), intent(in) :: version
  real(kind=c_double), intent(out) :: disp
  real(kind=c_double), intent(out) :: grads(3,natoms)

  type(dftd3_calc) :: calc
  type(dftd3_input) :: input

  call dftd3_init(calc, input)
  call dftd3_set_params(calc, pars, version)
  call dftd3_dispersion(calc, coords, izp, disp, grads)

end subroutine dftd3_dispersion_c
