import styled from 'styled-components';
import {
  COLOR_DARK,
  COLOR_TEAL,
  COLOR_LIGHT_GREY,
  COLOR_TEAL_DARK,
  COLOR_TEAL_VERY_DARK,
} from '../../constants';

const Form = styled.form`
  width: 600px;
  margin: 0 10px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  background-color: ${COLOR_TEAL_DARK};
  display: flex;
  flex-direction: column;
  text-align: center;
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
    background-color: ${COLOR_TEAL_VERY_DARK};
    border-radius: 10px;
    &::placeholder {
      opacity: 0;
    }
  }
  span {
    position: absolute;
    top: 0;
    left: 45px;
    transform: translateY(30px);
    font-size: 0.825em;
    transition-duration: 300ms;
  }
  :focus-within > span,
  input:not(:placeholder-shown) + span {
    color: ${COLOR_TEAL};
    transform: translateY(0px);
  }
`;

const ButtonsContainer = styled.div`
  display: flex;
  margin-top: 20px;
`;

const ButtonContainer = styled.span`
  display: flex;
  margin: auto auto 0 auto;
  flex-direction: column;
  align-items: center;
`;

const SubmitButton = styled.input`
  border: none;
  margin: 20px 20px 20px 20px;
  height: 40px;
  width: 230px;
  background-color: ${COLOR_LIGHT_GREY};
  border-radius: 20px;
  &:hover {
    background-color: ${COLOR_TEAL};
  }
`;

const Button = styled.button`
  border: none;
  margin: 10px 20px 20px 20px;
  height: 40px;
  width: 230px;
  background-color: ${COLOR_LIGHT_GREY};
  border-radius: 20px;
  &:hover {
    background-color: ${COLOR_TEAL};
  }
`;

const ButtonText = styled.span`
  width: 200px;
  margin-top: 10px;
`;

const Header = styled.h2`
  font-size: 30px;
  margin: 10px 0 0 40px;
`;

const HeaderContainer = styled.span`
  display: flex;
  width: 600px;
  height: 60px;
  margin: 10px 10px 0 10px;
  border-radius: 10px;
  background-color: ${COLOR_DARK};
  border-radius: 10px 10px 0 0;
`;

export {
  Form,
  FormLabel,
  SubmitButton,
  Header,
  HeaderContainer,
  Button,
  ButtonsContainer,
  ButtonContainer,
  ButtonText,
};
