import {useEffect, useRef, useState} from "react";
import {socketService} from "../services/socketService";

const Chat = () => {
    const [room, setRoom] = useState(null)
    const [socketClient, setSocketClient] = useState(null)
    const [messages, setMessages] = useState([])
    const [targetUser, setTargetUser] = useState(null)
    const roomInput = useRef();

    useEffect(() => {
        if (room) {
            socketItit(room).then(client => setSocketClient(client))
        }
    }, [room]);

    const socketItit = async (room) => {
        const {chat} = await socketService();
        const client = await chat(room);

        client.onopen = () => {
            console.log('chat socket connected');
        }

        client.onmessage = ({data}) => {
            console.log(data);
            const {message, user} = JSON.parse(data.toString());
            if (user&&user.includes('_')) {
                const [userId, username] = user.split('_');
                setMessages(prevState => [...prevState, {userId, username, message}])
            } else {
                console.log(user, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!');
                setMessages(prevState => [...prevState, {user, message}])
            }
        }

        return client
    }

    const roomHandler = () => {
        setRoom(roomInput.current.value)
    }

    const handleEnterKey = (e) => {
        if (e.key == 'Enter') {
            console.log(targetUser, 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ');
            socketClient.send(JSON.stringify({
                data: targetUser ? {text:`Private ${e.target.value}`, userId:targetUser}: {text:e.target.value},
                action: !targetUser ? 'send_message' : 'send_private_message',
                request_id: new Date().getTime()
            }))
            e.target.value = ''
        }

    };

    return (
        <div>
            {
                !room
                    ?
                    <div>
                        <input type="text" ref={roomInput}/>
                        <button onClick={roomHandler}>Go to room</button>
                    </div>
                    :
                    <div>
                        {messages.map(msg => <div>
                            <span onClick={() => {
                                if (!targetUser) {
                                    setTargetUser(msg.userId)
                                } else {
                                    setTargetUser(null)
                                }
                                console.log(targetUser, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&');
                            }}>{msg.username||msg.userId||msg.user}</span>: {msg.message}
                        </div>)}
                        <input type="text" onKeyDown={handleEnterKey}/>
                    </div>
            }
        </div>
    );

};

export {Chat};