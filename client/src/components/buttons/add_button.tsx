import { Button } from "@chakra-ui/react";
import { BiPlus } from 'react-icons/bi'

type AddButtonProps = {
    title: String,
    onClick?: () => void,
}

function AddButton(props: AddButtonProps) {
    const { title, onClick } = props;
    return (
        <Button textAlign={'center'} colorScheme="purple" borderRadius={20} onClick={onClick}>
            <BiPlus color="white" />
            {title}
        </Button>
    )
}

export default AddButton;