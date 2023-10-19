import { Button, Input, Textarea } from "@chakra-ui/react"
import { useState } from "react"

function AccountTab() {
    const [pickedImageUrl, setPickedImageUrl] = useState('');
    const pickImage = () => {
        document.getElementById('pick-image-btn')?.click();
    }
    return (
        <div className="flex flex-col items-start p-4 space-y-2" >
            <h5>Your profile picture</h5>
            <div className="mb-1">
                <button className="w-[120px] h-[120px] space-y-0  border-black border-[0.5px] rounded-2xl border-dashed flex flex-col justify-center items-center"
                    onClick={pickImage}
                >
                    <img className="object-contain w-12 h-12 mt-0 mb-2" src="/images/upload_image_placeholder.png" />
                    <Input width={0} height={0} type="file" visibility={"hidden"} id='pick-image-btn' />
                    <span className="text-[12px] font-light">Upload your photo</span>
                </button>
            </div>
            <div className="w-full h-[1px] bg-[#E0E4EC]">
            </div>
            <div className="flex flex-col items-start w-full">
                <div className="grid grid-cols-2 w-full space-x-2 ">
                    {/* Left side */}
                    <div className="flex flex-col items-start">
                        <label htmlFor="fullname">Fullname</label>
                        <Input id="fullname" width={'full'} placeholder="Please enter the full name" />
                        <label htmlFor="username">Username</label>
                        <Input id="username" width={'full'} placeholder="Please enter your username" />
                    </div>

                    {/* Right side */}
                    <div className="flex flex-col items-start">
                        <label htmlFor="email">Email</label>
                        <Input id="email" width={'full'} placeholder="Please enter the email" type="email" />
                        <label htmlFor="phone_number">Phone</label>
                        <Input id="phone_number" width={'full'} type="tel" placeholder="Please enter your phone number" />
                    </div>
                </div>
                <label htmlFor="bio">Bio</label>
                <Textarea height={200} textAlign={'start'} id="bio" width={'full'} placeholder="Your bio's description  " />
            </div>
            <div className="flex flex-row justify-start space-x-2">
                <Button colorScheme="blue" paddingTop={2}>Update Profile</Button>
                <Button colorScheme="gray" paddingTop={2}>Reset </Button>
            </div>

        </div>
    )
}

export default AccountTab