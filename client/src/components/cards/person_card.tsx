type PersonCardProps = {
    name?: String,
    isUnknown?: boolean
}
function PersonCard(props: PersonCardProps) {
    const { isUnknown, name } = props;
    return (
        <div className="flex flex-col p-[10px] space-y-2  rounded-xl items-start border-[0.5px] border-[#B9B9B9]">
            <img className="m-0 w-[180px] h-[108px] object-cover" src={isUnknown ? '/images/person_placeholder_2.webp' : "/images/person_placeholder_1.jpg"} />
            <span className="text-[13px] font-bold text-black">{name}</span>
            <span className="text-[13px] font-normal text-black">{isUnknown ? 'Uknown' : 'Software Engineer'}</span>
        </div>
    )
}

export default PersonCard;