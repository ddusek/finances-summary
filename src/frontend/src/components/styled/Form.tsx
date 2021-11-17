import styled from 'styled-components';
import * as C from '../../utils/cssConstants';

const Container = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
`

const Form = styled.form`
  width: 100%;
  max-width: 600px;
  overflow:hidden;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  background-color: ${C.COLOR_TEAL_DARK};
  display: flex;
  flex-direction: column;
  text-align: center;

  .button {
    border: none;
    margin: 10px 20px 20px 20px;
    height: 40px;
    max-width: 230px;
    width: 100%;
    color: ${C.COLOR_DARK};
    line-height: 40px;
    font-size: ${C.FONT_SIZE_NORMAL};
    background-color: ${C.COLOR_FONT};
    border-radius: 20px;
    &:hover {
      background-color: ${C.COLOR_TEAL};
    }
  }

  .dropdown {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    outline: none;
    margin: 20px 20px 0 20px;
    width: calc(100% - 76px);
    padding: 5px 35px 5px 5px;
    font-size: ${C.FONT_SIZE_NORMAL};
    color: ${C.COLOR_FONT};
    border: none;
    background-color: ${C.COLOR_TEAL_VERY_DARK};
    background-image: url('/arrow-down.svg');
    background-size: 28px;
    background-position-x: 98%;
    background-position-y: 10px;
    background-repeat: no-repeat;
    border-radius: 10px;
    height: 37px;
  }

  .field-error {
    position: absolute;
    top: 25px;
    color: ${C.COLOR_RED};
    top: 30px;
    width: 150px;
    left: 405px;
    font-size: ${C.FONT_SIZE_NORMAL};
  }

  .field-border-error {
    border: 1px ${C.COLOR_RED} solid;
  }
`;

const FormLabel = styled.label`
  margin-bottom: 15px;
  position: relative;
  font-size: 20px;
  margin: 5px 0;
  input {
    width: calc(100% - 80px);
    font-size: 20px;
    height: 35px;
    margin: 20px 20px 0 20px;
    border: none;
    outline: none;
    background-color: ${C.COLOR_TEAL_VERY_DARK};
    border-radius: 10px;
    &::placeholder {
      opacity: 0;
    }
    &::-webkit-outer-spin-button,
    &::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }

    &[type='number'] {
      -moz-appearance: textfield;
    }
  }
  span.field-text {
    position: absolute;
    top: 0;
    left: 45px;
    transform: translateY(30px);
    font-size: ${C.FONT_SIZE_NORMAL};
    transition-duration: 300ms;
  }
  :focus-within > span.field-text,
  input:not(:placeholder-shown) + span {
    color: ${C.COLOR_TEAL};
    transform: translateY(0px);
  }
`;

const Buttons = styled.div`
  display: flex;
  margin-top: 20px;
  @media only screen and (max-width: ${C.MIN_TABLET_RES-1}px) {
    flex-direction: column;
  }
`;

const ButtonContainer = styled.span`
  display: flex;
  @media only screen and (min-width: ${C.MIN_TABLET_RES}px) {
    margin: auto;
    width: 230px;
  }
  flex-direction: column;
  align-items: center;
`;

const SubmitButton = styled.input`
  border: none;
  margin: 10px 20px 20px 20px;
  height: 40px;
  max-width: 230px;
  width: 100%;
  background-color: ${C.COLOR_FONT};
  font-size: ${C.FONT_SIZE_NORMAL};
  border-radius: 20px;
  &:hover {
    background-color: ${C.COLOR_TEAL};
    cursor: pointer;
  }
`;

const ButtonText = styled.span`
  max-width: 200px;
  width: 100%;
  min-height: 18px;

  &.submit-error {
    color: ${C.COLOR_RED};
  }

  &.submit-success {
    color: ${C.COLOR_TEAL};
  }
`;

const Header = styled.h2`
  font-size: 30px;
  margin: 10px 0 0 40px;
`;

const HeaderContainer = styled.span`
  display: flex;
  max-width: 600px;
  width: 100%;
  min-height: 60px;
  height: auto;
  overflow:hidden;
  border-radius: 10px;
  background-color: ${C.COLOR_DARK};
  border-radius: 10px 10px 0 0;
`;

export {
  Container,
  Form,
  FormLabel,
  SubmitButton,
  Header,
  HeaderContainer,
  Buttons,
  ButtonContainer,
  ButtonText,
};
